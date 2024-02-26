export const APICall = async (
  src: string,
  inputText: string,
  model: string,

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
    }),
  });

  if (res.status !== 200) {
    throw new Error(`API returned an error: ${res.statusText}`);
  }

  const data = await res.json(); // Parse the JSON response body

  return data;
};
