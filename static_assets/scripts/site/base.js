if (window.Sentry) {
  Sentry.init({
    dsn: "https://90a1a7dd37134928b5a981eeb3a20293@o91052.ingest.sentry.io/198396",
    release: "routechoices@" + window.local.siteVersion,
  });
}

if (needFlagsEmojiPolyfill) {
  document.body.classList.add("flags-polyfill");
}

console.log(`___________________________
|                _____     |
|              / ____  \\   |
|             / /  _ \\  \\  |
|    _____   | |  //  | |  |
|  / ____  \\  \\ \\//_ / /   |
| / /  _ \\  \\  \\  ___ /    |
|| |  //  | |  //  _____   |
| \\ \\//_ / /  // / ____  \\ |
|  \\  ___ /  // / /  _ \\  \\|
|  //       // | |  //  | ||
| //       //   \\ \\//_ / / |
|//       //     \\  ___ /  |
|/       //      //        |
|       //      //         |
|__________________________|

ROUTECHOICES.COM
Version: ${window.local.siteVersion}`);
