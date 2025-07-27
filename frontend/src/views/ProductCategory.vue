<script setup lang="ts">
  import ProductThumbnail from '@/components/ProductThumbnail.vue';
  import { watch, ref, onMounted } from 'vue'
  import { useRoute, useRouter, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  const router = useRouter()
  var currentCategory = ref(route.params.product_category as string)
  var categoryProdAPIEndpoint = "/api/categories?category=" + currentCategory.value
  var dropdownArrow = "/static/backarrow.png"

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
    image: string[];
    description: string;
  }

  const productsInCategory = ref<Product[]>([])
  const emptyCategory = ref(true)

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
      emptyCategory.value = productsInCategory.value.length === 0
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
  <div class="backbutton">
    <button @click="router.go(-1)"><img id="backbuttonimg" :src="dropdownArrow"></img>Back</button>
  </div>
  <div v-if="emptyCategory" class="product-category-no-products-page">
    <p>There are no items to show for this category at the moment. Please check later.</p>
  </div>
  <div v-else class="product-category-body">
    <div v-for="product in productsInCategory">
      <ProductThumbnail :product-category="currentCategory" :product="product"/>
    </div>
  </div>
</template>

<style>
  .product-category-body {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding-left: var(--horizontal-page-padding);
    padding-right: var(--horizontal-page-padding);
    padding-top: 2rem;
    padding-bottom: 2rem;
    min-height: var(--home-height);
    box-sizing: border-box;
  }

  .product-category-no-products-page {
    justify-content: center;
    height: 100vh;
    font-size: 1.25rem;
    padding: 5%;
    display: flex;
  }

  #backbuttonimg {
    width: auto;
    height: max-content;
  }

  .backbutton {
    padding-top: 25px;
    padding-left: var(--horizontal-page-padding);
    padding-right: var(--horizontal-page-padding);
  }

  .backbutton button {
    display: flex;
    align-items: center;
    background-color: transparent;
    border: none;
    font-size: 1rem;
  }

</style>

