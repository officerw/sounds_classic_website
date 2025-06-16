
<script setup lang="ts">
    import { RouterLink } from 'vue-router'
    import { ref } from "vue"
    import RouterDropdown from './RouterDropdown.vue';

    const productCategories = ref([
        { id: 1, routerPath: "/turntables", text: "Turntables"},
        { id: 2, routerPath: "/preampfliers", text: "Preamplifiers"},
        { id: 3, routerPath: "/", text: "Power Amplifiers"},
        { id: 4, routerPath: "/", text: "Integrated Amplifiers"},
        { id: 5, routerPath: "/", text: "Equalizers"},
        { id: 6, routerPath: "/", text: "Tuners"},
        { id: 7, routerPath: "/", text: "Disc Players"},
        { id: 8, routerPath: "/", text: "8 track players"},
        { id: 9, routerPath: "/", text: "Reel to Reel Players"},

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
        height: inherit;
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
