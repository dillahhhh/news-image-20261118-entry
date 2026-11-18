// Entry program for news-image-20261118.
//
// The image is drawn at build time (see tools/render.py) and stored in this
// repository as assets/entry.png. This program only copies that file to the
// output path the harness asks for, so it needs no network and always writes
// the same bytes.
//
// The harness sets MAKEFUN_OUTPUT_DIR; without it we fall back to /output,
// which is the path the competition rules name.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";

const here = dirname(new URL(import.meta.url).pathname);
const asset = resolve(here, "assets", "entry.png");

const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
mkdirSync(outDir, { recursive: true });

const target = join(outDir, "entry.png");
copyFileSync(asset, target);
console.log(`wrote ${target}`);
