import { Model } from '@/types/types';
import { FC } from 'react';

interface Props {
  model: Model;
  onChange: (model: Model) => void;
}

export const ModelSelect: FC<Props> = ({ model, onChange }) => {
  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    onChange(e.target.value as Model);
  };

  return (
    <select
      className="h-[40px] w-[140px] rounded-md bg-[#1F2937] px-4 py-2 text-neutral-200 text-center"
      value={model}
      onChange={handleChange}
    >
      <option value="nllb">NLLB</option>
      <option value="opus">Opus-MT</option>
    </select>
  );
};
