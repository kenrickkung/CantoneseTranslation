export type Model = 'NLLB' | 'Opus-MT';

export interface TranslateBody {
  src: string;
  inputText: string;
  model: Model;
}

export interface TranslateResponse {
  outputText: string;
}
