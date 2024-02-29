import { FC } from 'react';

interface Props {
    paths: string[];
    selectedPath: string;
    onChange: (path: string) => void;
}

export const PathSelect: FC<Props> = ({ paths, selectedPath, onChange }) => {
  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    console.log("Selected path:", e.target.value);
    onChange(e.target.value);
  };

  return (
    <select
      className="h-[40px] w-[150px] rounded-md bg-[#1F2937] px-4 py-2 text-neutral-200 text-center"
      value={selectedPath}
      onChange={handleChange}
    >
      {paths.length > 0 ? (
          paths.map((path, _) => (
            <option key={path} value={path}>
              {path}
            </option>
          ))
        ) : (
          <option value="">-</option>
        )}
    </select>
  );
};