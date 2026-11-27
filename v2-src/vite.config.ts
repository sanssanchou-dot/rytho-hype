import path from "node:path"
import { defineConfig } from "vite"
import react from "@vitejs/plugin-react"
import tailwindcss from "@tailwindcss/vite"

// Built into ../v2 and served at /rytho-hype/v2/. Images stay in ../img (shared with v1), referenced as "../img/...".
export default defineConfig({
  base: "./",
  plugins: [react(), tailwindcss()],
  resolve: { alias: { "@": path.resolve(__dirname, "./src") } },
  build: { outDir: "../v2", emptyOutDir: true },
})
