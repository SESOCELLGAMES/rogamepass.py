import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Roapi.py",
  titleTemplate: "SESOCELL",
  description: "Gamepass Apis",
  lang: 'en-us',
  base: "/roapi.py/",
  themeConfig: {
    nav: [
      { text: 'Documentation', link: '/documentation/'},
      { text: 'Changelog', link: '/changelog/'},
      { text: 'Credits', link: '/credits/'},
    ],

    sidebar: {
      '/documentation': [
        {
          text: 'Roapi.py Docs',
          items: [
            { text: 'Roapi', link: '/documentation/'},
            { text: 'Gamepass Creator', link: '/documentation/create'},
            { text: 'Gamepass Buyer', link: '/documentation/buy'},
            { text: 'Gamepass Deletor', link: '/documentation/delete'},
            { text: 'Gamepass Editor', link: '/documentation/edit'},
            { text: 'Checking Own', link: '/documentation/checkown'},
          ]
        }
      ]
    },

    outline: [2, 3],


    search: {
      provider: 'local'
    },

    footer: {
      message: 'Made by sesocell and saveside (he did nothing but ok)',
    },

    socialLinks: [
      { icon: 'github', link: 'https://github.com/sesocell/roapi.py'}
    ]
  }
})
