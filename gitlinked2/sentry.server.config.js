// This file configures the initialization of Sentry on the server.
// The config you add here will be used whenever the server handles a request.
// https://docs.sentry.io/platforms/javascript/guides/nextjs/

import * as Sentry from "@sentry/nextjs";

throw new Error("hielo sentry");

Sentry.init({
  dsn: "https://a9d7f8c29a27f127683f198708a72f5d@o4506017113243648.ingest.sentry.io/4506017123991552",

  // Adjust this value in production, or use tracesSampler for greater control
  tracesSampleRate: 1,

  // Setting this option to true will print useful information to the console while you're setting up Sentry.
  debug: false,
});
