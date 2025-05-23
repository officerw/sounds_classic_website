<script setup lang="ts">
  import { RouterView, RouterLink } from 'vue-router'
  import { ref, computed } from "vue"
import HeaderNavBar from './components/HeaderNavBar.vue'

  // Set title of website
  const title = "Sounds Classic"

  // footer content
  const footer = "Copyright © 2025 Soundsclassic.com"
</script>

<template>
  <header>
    <RouterLink class="logo" to="/"><img alt="Sounds Classic Logo" class="logo" src="/static/logo_main.jpg"/></RouterLink>
    <HeaderNavBar/>
  </header>

  <RouterView />

  <!-- footer always present, containing authorship info for website -->
  <footer>
    <p class="footer">{{ footer }}</p>
  </footer>
</template>

<style scoped>
  .logo {
    height: inherit;
    max-height: var(--max-logo-size);
  }

  header {
    height: var(--header-height);
    width: 100%;
    padding: 0 10% 0 10%;
    align-items: center;
    display: flex;
    background-color: #000000;
    justify-content: start;
    flex-direction: var(--header-flex-direction);
  }

  footer {
    width: 100%;
    bottom:0;
    padding: 0 10% 0 10%;
    height: 4.5rem;
    background-color: #000000;
    color: white;
    text-align: center;
    display: flex;
    font-size: var(--normal-font-size);
    justify-content: center;
    align-items: center;
  }

  footer a {
    color: #00bf7d;
    text-decoration: none;
  }

  footer a:hover {
    background-color: rgba(0, 191, 125, 0.25);
  }
</style>
