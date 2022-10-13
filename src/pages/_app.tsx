import type { AppProps } from 'next/app'

// 1. import `NextUIProvider` component
import { NextUIProvider } from '@nextui-org/react';
import Header from '../lib/layout/header';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <NextUIProvider>
      <Header/>
      <Component {...pageProps} />
    </NextUIProvider>
  );
}

export default MyApp
