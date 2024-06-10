<script setup>
import { VPTeamMembers } from 'vitepress/theme'

const members = [
  {
    avatar: 'https://www.github.com/sesocell.png',
    name: 'sesocell',
    title: 'Creator',
    links: [
      { icon: 'github', link: 'https://github.com/sesocell' },
      { icon: 'twitter', link: 'https://x.com/sesocell' }
    ]
  },
  {
    avatar: 'https://www.github.com/saveside.png',
    name: 'saveside',
    title: 'UI/UX Designer for nothing',
    links: [
      { icon: 'github', link: 'https://github.com/saveside'},
      { icon: 'twitter', link: 'https://x.com/savedev1_'}
    ]
  },
]
</script>

# Our Team


<VPTeamMembers size="small" :members="members" />