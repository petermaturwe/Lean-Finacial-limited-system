/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'financial/templates/**/*.html',
    './node_modules/flowbite/**/.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

