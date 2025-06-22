
<script setup lang="ts">
    import { RouterLink } from 'vue-router'
    import { ref } from "vue"
    import RouterDropdown from './RouterDropdown.vue';

    const productCategories = ref([
        { id: 1, routerPath: { name: 'productcategories', params: { product_category: "turntables" } }, text: "Turntables"},
        { id: 2, routerPath: { name: 'productcategories', params: { product_category: "headphones" } }, text: "Headphones"},
        { id: 3, routerPath: { name: 'productcategories', params: { product_category: "speakers" } }, text: "Speakers"},
        { id: 4, routerPath: { name: 'productcategories', params: { product_category: "amplifiers" } }, text: "Amplifiers"},
        { id: 5, routerPath: { name: 'productcategories', params: { product_category: "receivers" } }, text: "Receivers"},
        { id: 6, routerPath: { name: 'productcategories', params: { product_category: "cdplayers" } }, text: "CD Players"},
        { id: 7, routerPath: { name: 'productcategories', params: { product_category: "cassetteplayers" } }, text: "Cassette Players"},
        { id: 8, routerPath: { name: 'productcategories', params: { product_category: "reel2reel" } }, text: "Reel-to-Reel"},
        { id: 9, routerPath: { name: 'productcategories', params: { product_category: "accessories" } }, text: "Accessories"},
    ])

</script>

<template>
    <nav class="nav-bar">
        <span id="productcategoriesdropdown">
            <RouterDropdown :menu-items="productCategories" title="Product Categories"/>
        </span>
        <RouterLink to="/">Services</RouterLink>
        <RouterLink to="/">Terms of Sale</RouterLink>
        <RouterLink to="/">About Us</RouterLink>
        <RouterLink to="/">Contact Us</RouterLink>
    </nav>
</template>

<style>
    nav {
        height: var(--nav-height);
        flex-direction: row;
        display: inline-flex;
    }

    nav a {
        text-decoration: none;
        align-items: center;
        color: white;
        padding-left: var(--header-nav-horizontal-padding);
        padding-right: var(--header-nav-horizontal-padding);
        height: inherit;
        min-height: var(--nav-min-height);
        display: flex;
        font-size: var(--header-nav-font-size);
    }

    nav a:hover {
        background-color: rgba(255, 255, 255, 0.25);
    }
</style>
