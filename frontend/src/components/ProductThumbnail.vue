<script setup lang="ts">
    import { RouterLink } from 'vue-router'
    import { defineProps } from 'vue'

    const IMAGES_PATH = import.meta.env.VITE_IMAGES_PATH

    const props = defineProps({
        product: {
            type: Object as () => {
                id: string
                itemNumber: string
                manufacturer: string
                model: string
                price: Number
                condition: string
                image: string[]
                description: string
            },
            required: true
        },
        productCategory: {
            type: String,
            required: true
        }
    })

</script>

<template>
    <div class="product-thumbnail">
        <RouterLink :to="{ name: 'productid', params: { product_category: productCategory, product_id: product.id } }">
            <img :src="'/api/product/image?img=ar_4x_grls.jpg'" :alt="product.manufacturer + ' ' + product.model" class="product-image" />
        </RouterLink>
        
        <h3 id="product-title">{{ product.manufacturer }} {{ product.model }}</h3>
        <h4 id="product-price">${{ product.price.toFixed(2) }}</h4>
        <p id="product-condition">Condition: {{ product.condition }}</p>
        <p id="product-description">Description: {{ product.description }}</p>
    </div>
</template>

<style scoped>
    .product-thumbnail {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 16px;
        text-align: left;
        width: 300px;
        height: 500px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        overflow: hidden;
    }

    #product-price {
        font-weight: bold;
        margin: 8px 0;
    }

    #product-condition {
        font-weight: bold;
    }

    img {
        width: 100%;
        height: auto
    }
</style>