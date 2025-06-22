<!--
    ROUTER DROPDOWN

    This a dropdown component where the router switches to a view based on 
    which option in the dropdown the user clicks on. This is a dropdown 
    that shows the different interactions between the pages (from
    Home to Georgia Rap Sheet for example)
--> 

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import { ref } from 'vue'

/*
    menuItem structure:
    - menuItem.id indicates the position of the menu
    item in the list of menuItems for the dropdown menu
    - menuItem.routerPath indicates where the Router
    should navigate to when clicked on. Review list of
    routerPaths in ../router/index.ts
    - menuItem.text is the string displayed to the user
    on the menu item within the dropdown menu
*/
interface MenuItem {
    id: number
    routerPath: string
    text: string
}

/*
    Input props for the RouterDropdown component:
    - menuItems (required), type: menuItem[]
        - Description: an array of menuItem's, where
        each menuItem outlines the order, router path,
        and display text for the menuItem in the 
        dropdown menu
    - title (required), type: String
        - Description: the text to be shown on the main
        dropdown button, the button that toggles the
        dropdown visibility.
*/
const props = defineProps({
    menuItems: {
        type: Array as () => MenuItem[],
        required: true
    },
    title: {
        type: String,
        required: true
    }
})

// Toggles whether the dropdown menu options are visible to the user
var isDropdownDisplayed = ref(false)
var dropdownArrow = "/static/downarrow_white.png"
function toggleDropdown() {
    isDropdownDisplayed.value = !isDropdownDisplayed.value

    // Switch dropdown arrow image
    if (dropdownArrow === "/static/downarrow_white.png") {
        dropdownArrow = "/static/uparrow_white.png"
    } else {
        dropdownArrow = "/static/downarrow_white.png"
    }
}
</script>

<template>
    <!--
        The RouterDropdown is a component dropdown menu that allows users to select which
        view from ../views should be shown
    -->
    <div class="dropdown">
        <!--
            Using the toggleDropdown function, the button toggles whether the dropdown options
            are visible
        -->
        <div class="dropdownbuttoncontainer">
            <button class="dropdownbutton" @click="toggleDropdown">{{ title }} <img :src=dropdownArrow id="dropdownarrow"></button>
        </div>
        
        <!--
            Defines an unordered list containing the RouterLink buttons to change the view
            displayed from the menuItems prop
        -->
        <div v-if="isDropdownDisplayed" class="dropdownmenu">
            <ul>
                <li v-for="menuItem in props.menuItems" :key="menuItem.id">
                    <RouterLink v-bind:to=menuItem.routerPath>{{ menuItem.text }}</RouterLink>
                </li>
            </ul>
        </div>
    </div>
</template>

<style scoped>
.dropdown {
    width:100%;
    height:100%;
}


.dropdownbuttoncontainer {
    width: 100%;
    height: 100%;
    position: relative;
}

.dropdownbutton {
    position: relative;
    border: none;
    background-color: inherit;
    color: white;
    font-size: var(--header-nav-font-size);
    height:100%;
    width:100%;
    cursor: pointer;
    justify-content: center;
    align-items: center;
    display: flex;
    flex-direction: column;
}

.dropdownmenu {
    display: inline-block;
    background-color: lightgray;
    height: fit-content;
    width: 100%;
    z-index: 10000 !important;
    position: relative;
}

.dropdownmenu ul {
    max-height: 15rem;
    height: fit-content;
    overflow: auto;
    padding-bottom: 1px;
}

.dropdownmenu li {
    list-style-type: none;
    text-align: center;
    padding-top: 0.25rem;
    padding-bottom: 0.25rem;
}

.dropdownmenu ul {
    width: 100%;
    padding: 0;
    padding-bottom: 1px;
}

img {
    height: 20%;
    width: auto;
    margin: 5px;
}

a {
    padding: 0;
    display: block;
    width: 100%;
    height: 100%;
    color:black;
    text-wrap: initial;
}

a:hover {
    background-color: gray;
}
</style>