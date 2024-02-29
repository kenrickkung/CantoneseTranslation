export type Model = 'NLLB' | 'Opus-MT';

export interface TranslateBody {
  src: string;
  inputText: string;
  model: Model;
  selectedPath: string;
}

export interface TranslateResponse {
  outputText: string;
}

export interface ModelBody {
  model: string;
  src: string;
}

export interface ModelResponse {
  paths: string[];
}
