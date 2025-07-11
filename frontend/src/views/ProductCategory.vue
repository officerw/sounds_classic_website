<script setup lang="ts">
  import ProductThumbnail from '@/components/ProductThumbnail.vue';
  import { watch, ref, onMounted } from 'vue'
  import { useRoute, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  var currentCategory = ref(route.params.product_category as string)
  var categoryProdAPIEndpoint = "/api/categories?category=" + currentCategory.value

  // watch for changes in the product category to update
  // product thumbnails
  onBeforeRouteUpdate(async (to, from) => {
    // react to route changes...
    currentCategory.value = to.params.product_category as string
    categoryProdAPIEndpoint = "/api/categories?category=" + currentCategory.value
    await getProductCategories()
  })

  interface Product {
    id: string;
    itemNumber: string;
    manufacturer: string;
    model: string;
    price: Number;
    condition: string;
    imageUrl: string;
    description: string;
  }

  const productsInCategory = ref<Product[]>([])

  async function getProductCategories() {
    try {
      const response = await fetch(categoryProdAPIEndpoint, {
        method: "GET"
      });
      if (!response.ok) {
        throw new Error("Failed to get products in specific category");
      }
      var categories = await response.json()
      productsInCategory.value = categories.map((product: Product) => product)
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
  <div class="product-category-body">
    <div v-for="product in productsInCategory">
      <ProductThumbnail :product-category="currentCategory" :product="product"/>
    </div>
  </div>
</template>

<style>
  .product-category-body {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    padding-left: var(--horizontal-page-padding);
    padding-right: var(--horizontal-page-padding);
    padding-top: 2rem;
    padding-bottom: 2rem;
    min-height: var(--home-height);
    box-sizing: border-box;
  }

</style>

