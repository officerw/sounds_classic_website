import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Product from '@/views/Product.vue'
import ProductCategory from '@/views/ProductCategory.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/productcategories/:product_category',
      name: 'productcategories',
      component: ProductCategory
    },
    {
      path: '/productcategories/:product_category/productid/:product_id',
      name: 'productid',
      component: Product
    }
  ]
})

export default router
