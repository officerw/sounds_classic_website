
<script setup lang="ts">
    import { RouterLink } from 'vue-router'
    import { ref, computed, onMounted } from "vue"
    import RouterDropdown from './RouterDropdown.vue';

    // accept the menu items for this dropdown menu
    const props = defineProps({
        productCategories: {
            type: Array as () => String[],
            required: true
        }
    })

    // Map the array of category strings to menu item objects
    const productCategoryMenuItems = computed(() =>
        props.productCategories.map((category, idx) => ({
            id: idx + 1,
            routerPath: { name: 'productcategories', params: { product_category: String(category) } },
            text: String(category)
        }))
    )
</script>

<template>
    <nav class="nav-bar">
        <span id="productcategoriesdropdown">
            <RouterDropdown :menu-items="productCategoryMenuItems" title="Product Categories"/>
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
