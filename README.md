Minimal Sqlite WASM example with persistent storage in OPFS and Async API


Important!
==========

Serve content using following headers, otherwise won't work:

    Cross-Origin-Embedder-Policy: require-corp
    Cross-Origin-Opener-Policy: same-origin

For reason see "Achtung: COOP and COEP HTTP Headers" in: https://sqlite.org/wasm/doc/trunk/persistence.md#coop-coep


Run (Serve locally)
===================

  python3 server-with-headers.py


Update Sqlite version
=====================

1) Download "WebAssembly & JavaScript" from https://www.sqlite.org/download.html
2) unpack in root of project
3) change src of import tag to new script in index.html ( ??? /jswasm/sqlite3-worker1-promiser.js)


