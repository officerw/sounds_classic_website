<script setup lang="ts">
    import ProductCategory from '@/views/ProductCategory.vue'
import { RouterLink } from 'vue-router'

    const props = defineProps({
        product: {
            type: Object as () => {
                id: string
                itemNumber: string
                manufacturer: string
                model: string
                price: Number
                condition: string
                imageUrl: string
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
            <img :src="product.imageUrl" :alt="product.manufacturer + ' ' + product.model" class="product-image" />
        </RouterLink>
        
        <h3 class="product-title">{{ product.manufacturer }} {{ product.model }}</h3>
        <p class="product-price">${{ product.price.toFixed(2) }}</p>
        <p class="product-condition">Condition: {{ product.condition }}</p>
        <p class="product-description">Description: {{ product.description }}</p>
    </div>
</template>

<style scoped>
    .product-thumbnail {
        border: 1px solid #ccc;
        border-radius: 8px;
        padding: 16px;
        text-align: center;
        max-width: 300px;
        max-height: 500px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    img {
        width: 100%;
        height: auto
    }
</style>