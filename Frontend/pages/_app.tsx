import { useEffect } from 'react';
import "@/styles/globals.css";
import type { AppProps } from "next/app";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

function App({ Component, pageProps }: AppProps<{}>) {
  useEffect(() => {
    // This assumes you have a specific class or directly set styles for the body
    document.body.classList.add('body-background');

    return () => {
      document.body.classList.remove('body-background');
    };
  }, []);

  return (
    <main className={inter.className}>
      <Component {...pageProps} />
    </main>
  );
}

export default App;
