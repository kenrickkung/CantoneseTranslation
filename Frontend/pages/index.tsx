import { LanguageSelect } from '@/components/LanguageSelect';
import { ModelSelect } from '@/components/ModelSelect';
import { PathSelect } from '@/components/PathSelect';
import { TextBlock } from '@/components/TextBlock';
import { Model, TranslateBody, ModelBody } from '@/types/types';
import Head from 'next/head';
import { useEffect, useState } from 'react';

export default function Home() {
  const [src, setSrc] = useState<string>('zh');
  const [tgt, setTgt] = useState<string>('en');
  const [inputText, setInputText] = useState<string>('');
  const [outputText, setOutputText] = useState<string>('');
  const [model, setModel] = useState<Model>('nllb');
  const [paths, setPaths] = useState<string[]>([]);
  const [selectedPath, setSelectedPath] = useState<string>(paths[0] || "");
  const [loading, setLoading] = useState<boolean>(false);
  const [hasTranslated, setHasTranslated] = useState<boolean>(false);

  const handleModelType = async () => {
    try {
      const body: ModelBody = {
        model,
        src,
      };

      const response = await fetch('/api/models', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        throw new Error('Something went wrong with the translation service.');
      }

      const { model_path } = await response.json();
      setPaths(model_path);

    } catch (error){
      console.error(error);
      alert('Something went wrong.');
    }
  }

  const handleTranslate = async () => {
    if (src === tgt) {
      alert('Please select different languages.');
      return;
    }

    if (!inputText) {
      alert('Please enter some text.');
      return;
    }

    setLoading(true);
    setOutputText('');

    try {
      const body: TranslateBody = {
        src,
        inputText,
        model,
        selectedPath,
      };

      const response = await fetch('/api/translate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
      });

      if (!response.ok) {
        throw new Error('Something went wrong with the translation service.');
      }

      const { translatedText } = await response.json();
      setOutputText(translatedText);
      setHasTranslated(true);
      copyToClipboard(outputText);
    } catch (error) {
      console.error(error);
      alert('Something went wrong.');
    } finally {
      setLoading(false);
    }
  };

  const copyToClipboard = (text: string) => {
    const el = document.createElement('textarea');
    el.value = text;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
  };

  useEffect(() => {
    document.body.classList.add("body-background");
  }, [])

  useEffect(() => {
    if (src === 'zh') {
      setTgt('en');
    }

    if (src === 'en') {
      setTgt('zh');
    }
  }, [src])

  useEffect(() => {
    if (paths.length > 0) {
      setSelectedPath(paths[0]);
    }
  }, [paths]);

  useEffect(() => {
    if (hasTranslated) {
      handleTranslate();
    }
  }, [hasTranslated]);

  useEffect(() => {
    if (model && src) {
      handleModelType();
    }
  }, [model, src]);
  return (
    <>
      <Head>
        <title>Cantonese Translator</title>
        <meta
          name="description"
          content="Use Different model to translate text from Cantonese to English."
        />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <div className="flex h-full min-h-screen flex-col items-center bg-[#0E1117] px-4 pb-20 text-neutral-200 sm:px-10">
        <div className="mt-10 flex flex-col items-center justify-center sm:mt-20">
          <div className="block text-transparent bg-clip-text bg-gradient-to-r 
          from-blue-500 via-pink-500 to-blue-500 text-4xl font-bold">Cantonese Translator</div>
        </div>

        <div className="mt-2 flex items-center space-x-2">
          <ModelSelect model={model} onChange={(value) => setModel(value)} />
          {paths.length > 0 && (
          <PathSelect paths={paths} selectedPath={selectedPath} onChange={setSelectedPath} />
          )}

          <button
            className="w-[140px] cursor-pointer rounded-md bg-violet-500 px-4 py-2 font-bold hover:bg-violet-600 active:bg-violet-700"
            onClick={() => handleTranslate()}
            disabled={loading}
          >
            {loading ? 'Translating...' : 'Translate'}
          </button>
        </div>

        <div className="mt-2 text-center text-xs">
          {loading
            ? 'Translating...'
            : hasTranslated
            ? 'Translated!'
            : 'Enter some text and click "Translate"'}
        </div>

        <div className="mt-6 flex w-full max-w-[1200px] flex-col justify-between sm:flex-row sm:space-x-4">
          <div className="h-100 flex flex-col justify-center space-y-2 sm:w-2/4">
            <div className="text-center text-xl font-bold">Input</div>

            <LanguageSelect
              language={src}
              onChange={(value) => {
                setSrc(value);
                setHasTranslated(false);
                setInputText('');
                setOutputText('');
              }}
            />            
              <TextBlock
                text={inputText}
                editable={!loading}
                onChange={(value) => {
                  setInputText(value);
                  setHasTranslated(false);
                }}
              />
          </div>
          <div className="mt-8 flex h-full flex-col justify-center space-y-2 sm:mt-0 sm:w-2/4">
            <div className="text-center text-xl font-bold">Output</div>

            <LanguageSelect
              language={tgt}
              onChange={(value) => {
                setTgt(value);
                setOutputText('');
              }}
              disabled={true}
            />
              <TextBlock text={outputText} />
          </div>
        </div>
      </div>
    </>
  );
}
