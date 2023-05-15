import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'build', // output built files to 'build' directory
  },
  server: {
    host: '0.0.0.0',
    port: 3000, 
  },
});
