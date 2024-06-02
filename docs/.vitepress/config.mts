import { defineConfig } from 'vitepress'

export default defineConfig({
  title: "Roapi.py",
  titleTemplate: "SESOCELL",
  description: "Gamepass Apis",
  lang: 'en-us',

  themeConfig: {
    nav: [
      { text: 'Documentation', link: '/documentation/'},
      { text: 'Changelog', link: '/changelog/'},
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
          ]
        },
      ],
      '/guides': [
        {
          text: 'Guides',
          items: [
            { text: 'Profile Stores', link: '/guides/' },
            { text: 'Profiles', link: '/guides/profiles' },
            { text: 'Leaderstats Setup', link: '/guides/leaderstats' },
            { text: 'Global Keys', link: '/guides/globalkeys' },
          ]
        },
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
