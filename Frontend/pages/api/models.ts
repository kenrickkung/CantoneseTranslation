import { ModelBody } from '@/types/types';
import { GetModel } from '@/utils';

export const config = {
  runtime: 'edge',
};

const handler = async (req: Request): Promise<Response> => {
  try {
    const { model, src} =
      (await req.json()) as ModelBody;

    const response = await GetModel(
      model,
      src,
    );

    return new Response(JSON.stringify(response), {
      headers: { 'Content-Type': 'application/json' },
      status: 200,
    });
  } catch (error) {
    console.error(error);
    return new Response(JSON.stringify({ error: 'Error processing your request' }), {
      headers: { 'Content-Type': 'application/json' },
      status: 500,
    });
  }
};

export default handler;
