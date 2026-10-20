/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: ['class', '[data-theme="dark"]'],
  theme: {
    extend: {
      colors: {
        maki: {
          paper: 'var(--paper)',
          sheet: 'var(--sheet)',
          well: 'var(--well)',
          ink: 'var(--ink)',
          muted: 'var(--muted)',
          line: 'var(--line)',
          blue: 'var(--blue)',
          blueBg: 'var(--blue-bg)',
          green: 'var(--green)',
          greenBg: 'var(--green-bg)',
          amber: 'var(--amber)',
          amberBg: 'var(--amber-bg)',
          purple: 'var(--purple)',
          red: 'var(--red)',
        }
      },
      fontFamily: {
        display: ['"Noto Serif SC"', '"Source Han Serif SC"', '"Songti SC"', '"STSong"', '"Times New Roman"', 'Georgia', 'serif'],
        body: ['"PingFang SC"', '"Noto Sans SC"', '"Source Han Sans SC"', '"Hiragino Sans GB"', '"Microsoft YaHei"', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'Consolas', '"Liberation Mono"', 'Menlo', 'Courier', 'monospace'],
      }
    },
  },
  plugins: [],
}
