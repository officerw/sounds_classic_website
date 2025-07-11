<script setup lang="ts">
  import { RouterView, RouterLink, stringifyQuery } from 'vue-router'
  import { ref, computed, onMounted } from "vue"
  import HeaderNavBar from './components/HeaderNavBar.vue'

  // Set title of website
  const title = "Sounds Classic"

  // footer content
  const footer = "Copyright © 2025 Soundsclassic.com"

  // set categories list
  const productCategories = ref<string[]>([])

  const PROD_CATEGORIES_API_ENDPOINT = "/api/categories"
  async function getProductCategories() {
    try {
      const response = await fetch(PROD_CATEGORIES_API_ENDPOINT, {
        method: "GET"
      });
      if (!response.ok) {
        throw new Error("Failed to get product categories");
      }
      var categories = await response.json()
      productCategories.value = categories.map((category: string) => String(category))
    } catch (error) {
      console.error("Error fetching product categories:", error);
      return [];
    }
  }

  onMounted(() => {
    getProductCategories()
  })
</script>

<template>
  <header>
    <RouterLink class="logo" to="/"><img alt="Sounds Classic Logo" class="logo" src="/static/logo_main.jpg"/></RouterLink>
    <HeaderNavBar :product-categories="productCategories"/>
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
    justify-content: center;
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
