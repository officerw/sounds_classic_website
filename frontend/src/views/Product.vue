<script setup lang="ts">
    import { onMounted, ref } from 'vue'
    import { useRoute, useRouter } from 'vue-router'
    import 'vue3-carousel/carousel.css'
    import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'

    const carouselConfig = {
        itemsToShow: 1,
        wrapAround: false
    }

    const route = useRoute()
    const router = useRouter()
    var productId = ref(route.params.product_id as string)
    var productAPIEndpoint = `/api/products?id=${productId.value}`
    var dropdownArrow = "/static/backarrow.png"

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

    const product = ref<Product>({
        id: "",
        itemNumber: "",
        manufacturer: "",
        model: "",
        price: 0,
        condition: "",
        imageUrl: "",
        description: ""
    })

    const images = Array.from({ length: 2 }, (_, index) => ({
        id: index + 1,
        url: `/api/product/image/main-carousel?n=${Math.floor(Math.random() * 1000)}`,
    }))

    async function getProduct() {
        try {
            const response = await fetch(productAPIEndpoint, {
                method: "GET"
            });
            if (!response.ok) {
                throw new Error("Failed to get products in specific category");
            }
            var resultProduct = await response.json()
            product.value = resultProduct
        } catch (error) {
            console.error("Error fetching product categories:", error);
            return [];
        }
    }

    onMounted(() => {
        getProduct()
    })

</script>

<template>
    <div class="backbutton">
        <button @click="router.go(-1)"><img id="backbuttonimg" :src="dropdownArrow"></img>Back</button>
    </div>
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
            <h1 class="product-title">{{ product.manufacturer }} {{ product.model }}</h1>
            <h3 class="product-manufacturer">Manufacturer: {{ product.manufacturer }}</h3>
            <h3 class="product-model">Model: {{ product.model }}</h3>
            <br>
            <hr>
            <br>
            <h2 class="product-price">Price: ${{ product.price.toFixed(2) }}</h2>
            <br>
            <h3 class="product-description">Description: {{ product.description }}</h3>
            <h3 class="product-condition">Condition: {{ product.condition }}</h3>
        </div>
        <div class="two"></div>
        <div class="order-info">
            <h3>Complete order by contacting us directly.</h3>
            <br>
            <h3>Shipping costs will vary based on weight, size, and destination. Before shipment, items undergo quality control to verify 100% functionality and are then packed securely for safe delivery. Allow 48-72 hours for processing and shipping.</h3>
        </div>
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