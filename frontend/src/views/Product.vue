<script setup lang="ts">
    import { ref } from 'vue'
    import { useRoute, onBeforeRouteUpdate } from 'vue-router'
    import 'vue3-carousel/carousel.css'
    import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

    const carouselConfig = {
        itemsToShow: 1,
        wrapAround: false
    }

    const route = useRoute()
    var currentCategory = ref(route.params.product_category as string)
    var productId = ref(route.params.product_id as string)
    
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

    const images = Array.from({ length: 1 }, (_, index) => ({
        id: index + 1,
        url: sampleProduct.value.imageUrl,
    }))

    // watch for changes in the product category to update
    // product thumbnails
    onBeforeRouteUpdate(async (to, from) => {
        // react to route changes...
        currentCategory.value = to.params.product_category as string
        sampleProduct.value.imageUrl = `https://picsum.photos/seed/${currentCategory.value}/800/600`
        sampleProduct.value.manufacturer = `${currentCategory.value} manufacturer`
        sampleProduct.value.model = `${currentCategory.value} model`
    })

</script>

<template>
    <div class="product-body">
        <div class="product-image">
            <Carousel v-bind="carouselConfig">
                <Slide v-for="image in images" :key="image.id">
                    <img :src="image.url" alt="image">
                </Slide>

                <template #addons>
                    <Navigation />
                    <Pagination />
                </template>
            </Carousel>
        </div>
        <div class="product-title-div">
            <h1 class="product-title">{{ sampleProduct.manufacturer }} {{ sampleProduct.model }}</h1>
            <h3 class="product-manufacturer">Manufacturer: {{ sampleProduct.manufacturer }}</h3>
            <h3 class="product-model">Model: {{ sampleProduct.model }}</h3>
            <h3 class="product-number">Item #: {{ sampleProduct.itemNumber }}</h3>
            <br>
            <hr>
            <br>
            <h2 class="product-price">Price: ${{ sampleProduct.price.toFixed(2) }}</h2>
            <br>
            <h3 class="product-description">Description: {{ sampleProduct.description }}</h3>
            <h3 class="product-condition">Condition: {{ sampleProduct.condition }}</h3>
        </div>
        <div class="two"></div>
        <div class="three"></div>
        <div class="four"></div>
    </div>
</template>

<style scoped>

    .product-title-div {
        grid-column: var(--product-title-column);
        grid-row: var(--product-title-row);
    }

    .product-body {
        display: grid;
        grid-template-columns: var(--product-view-grid-template-columns);
        grid-template-rows: var(--product-view-grid-template-rows);
        padding-left: var(--horizontal-page-padding);
        padding-right: var(--horizontal-page-padding);
        padding-top: 2rem;
        padding-bottom: 2rem;
        min-height: var(--home-height);
        box-sizing: border-box;
    }


    .product-image {
        grid-column: 1;
        grid-row: 1;
        width: 100%;
        height: 100%;
        box-sizing: border-box;
        display: flex;
        flex-direction: column;
        min-width: 0;
        min-height: 0;
        overflow: hidden;
    }

    .carousel,
    .carousel__viewport {
        width: 100% !important;
        height: 100% !important;
        min-width: 0 !important;
        min-height: 0 !important;
        box-sizing: border-box;
        overflow: hidden;
        display: flex;
    }

    .carousel__slide {
        width: 100% !important;
        height: 100% !important;
        min-width: 0 !important;
        min-height: 0 !important;
        display: flex;
        padding: 1.5rem;
        align-items: center;
        justify-content: center;
    }

    .carousel__slide img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
        min-width: 0;
        min-height: 0;
    }

</style>