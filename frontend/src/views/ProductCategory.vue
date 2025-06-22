<script setup lang="ts">
  import ProductThumbnail from '@/components/ProductThumbnail.vue';
  import { watch, ref } from 'vue'
  import { useRoute, onBeforeRouteUpdate } from 'vue-router'

  const route = useRoute()
  var currentCategory = ref(route.params.product_category as string)

  // watch for changes in the product category to update
  // product thumbnails
  onBeforeRouteUpdate(async (to, from) => {
    // react to route changes...
    currentCategory.value = to.params.product_category as string
    sampleProduct.value.imageUrl = `https://picsum.photos/seed/${currentCategory.value}/800/600`
    sampleProduct.value.manufacturer = `${currentCategory.value} manufacturer`
    sampleProduct.value.model = `${currentCategory.value} model`
  })

  
  const sampleProduct = ref({
    id: '1',
    itemNumber: '1028',
    manufacturer: `${currentCategory.value} manufacturer`,
    model: `${currentCategory.value} model`,
    price: 999.99,
    condition: 'Used - Excellent',
    imageUrl: `https://picsum.photos/seed/${currentCategory.value}/800/600`,
    description: "Newer Sharp BD-HP25U Blu Ray DVD/CD Player. Comes w/ Remote. Ex. Cond. 8.9"
  })
  const sampleProducts = ref(Array(20).fill(sampleProduct.value))

</script>

<template>
  <div class="product-category-body">
    <div v-for="product in sampleProducts">
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

