export const Translate = async (
  src: string,
  inputText: string,
  model: string,
  selectedPath: string,

) => {
  const res = await fetch(`http://127.0.0.1:5000/translate`, {
    headers: {
      'Content-Type': 'application/json',
    },
    method: 'POST',
    body: JSON.stringify({
      text : inputText,
      model : model,
      src : src,
      path: selectedPath,
    }),
  });

  if (res.status !== 200) {
    throw new Error(`API returned an error: ${res.statusText}`);
  }

  const data = await res.json(); // Parse the JSON response body

  return data;
};

export const GetModel = async (
  model: string,
  src: string,

) => {
  const res = await fetch(`http://127.0.0.1:5000/models`, {
    headers: {
      'Content-Type': 'application/json',
    },
    method: 'POST',
    body: JSON.stringify({
      model_type : model,
      src : src,
    }),
  });

  if (res.status !== 200) {
    throw new Error(`API returned an error: ${res.statusText}`);
  }

  const data = await res.json(); // Parse the JSON response body

  return data;
};
