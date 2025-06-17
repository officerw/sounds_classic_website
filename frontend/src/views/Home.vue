<!--
  Home

  This page contains the body of the home page for the Sounds Classic Website
-->

<script setup lang="ts">
import { ref } from "vue"

const preloadedText = ref("At Soundsclassic.com, We Specialize in the Service and Restoration of Vintage Stereo Receivers, Amplifiers, Turntables, Tube Equipment and Speakers. We sell Vintage Stereo Equipment, High-end Audio Systems and Speakers. 40 Years of Trusted Audio Service Experience. Hi-Fi Audio Sales, Repair and Restoration in Rockford IL")
</script>

<template>
  <!-- body to contain all home page content below header and above footer -->
  <div class="home-body">
    <div class="text-box-container">
      <label class="text-box-label">Welcome Message</label>
      <p class="info-text">{{ preloadedText }}</p>
    </div>
  </div>
</template>

<style>
.home-body {
  width: 100%;
  padding-top: 0;
  padding-bottom: 0;
  padding-left: var(--horizontal-page-padding);
  padding-right: var(--horizontal-page-padding);
  min-height: var(--home-height);
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;
  gap: 2rem;
}

.text-box-container {
  width: 100%;
  max-width: 700px;
  display: flex;
  flex-direction: column;
}

.text-box-label {
  font-size: 1.1rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.info-text {
  background-color: #f9f9f9;
  border: 1px solid #ccc;
  border-radius: 6px;
  padding: 1rem;
  font-size: 1rem;
  color: #333;
  line-height: 1.5;
}
</style>