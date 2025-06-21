<script setup lang="ts">
    import 'vue3-carousel/carousel.css'
    import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

    const images = Array.from({ length: 10 }, (_, index) => ({
        id: index + 1,
        url: `https://picsum.photos/seed/${Math.random()}/800/600`,
    }))

    const carouselConfig = {
        itemsToShow: 2.5,
        wrapAround: true
    }
</script>

<template>
    <Carousel v-bind="carouselConfig">
        <Slide v-for="image in images" :key="image.id">
            <img :src="image.url" alt="image">
        </Slide>

        <template #addons>
            <Navigation />
            <Pagination />
        </template>
    </Carousel>
</template>

<style>
    .carousel {
        height: 100%;
    }

    .carousel__next {
        right: 15%;
    }

    .carousel__prev {
        left: 15%;
    }

    .carousel__next,
    .carousel__prev {
        background: rgba(0, 0, 0, 0.3);
        border-radius: 50%;
        width: 40px;
        height: 40px;
        color: white;
    }

    .carousel__next:hover,
    .carousel__prev:hover {
        color: red;
    }

    .carousel__pagination-button {
        height: 5px;
        width: 10px;
        border-radius: 5px;
        background-color: white;
    }
    .carousel__pagination-button--active {
        background-color: rgb(230, 48, 48);
    }

</style>