import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "rogamepass.py",
  titleTemplate: "SESOCELL",
  description: "Gamepass Apis",
  lang: 'en-us',
  base: "/rogamepass.py/",
  themeConfig: {
    nav: [
      { text: 'Documentation', link: '/documentation/'},
      { text: 'Changelog', link: '/changelog/'},
      { text: 'Credits', link: '/credits/'},
    ],

    sidebar: {
      '/documentation': [
        {
          text: 'rogamepass.py Docs',
          items: [
            { text: 'rogamepass', link: '/documentation/'},
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
      { icon: 'github', link: 'https://github.com/sesocell/rogamepass.py'}
    ]
  }
})
