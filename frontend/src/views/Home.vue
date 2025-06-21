<script setup lang="ts">
import { ref } from "vue"

const preloadedText = ref("At Soundsclassic.com, We Specialize in the Service and Restoration of Vintage Stereo Receivers, Amplifiers, Turntables, Tube Equipment and Speakers. We sell Vintage Stereo Equipment, High-end Audio Systems and Speakers. 40 Years of Trusted Audio Service Experience. Hi-Fi Audio Sales, Repair and Restoration in Rockford IL")

const featuredProductText = ref(`The Intelligent Audio M8 Bluetooth Adapter -
Do you want to connect your Phone or other Streaming Music Devices to your Vintage Stereo?
Now you can with The New Intelligent Audio M8 Bluetooth Adapter!
What a Great Stocking Stuffer! Just in Time for Christmas. Only $39.95

First and Formost- This one Sounds Really Great! So Easy to Connect and Operate.
Intelligent Digital Display in a Small foot print, only 3.5 x 3 in. with Remote Control.
Transmits and Receives Bluetooth 5.0 Analog and Digital I/O, 10 meters distance.

Only $39.95 while supplies last!`)
</script>

<template>
  <div class="home-body">
    <aside class="sidebar">
      <label class="text-box-label">Store Hours</label>
      <p class="info-text">
        Tues:Appointments only<br />
        Wed-Fri: 10am – 6pm<br />
        Sun - Mon: Closed <br />
        Tuesdays are by appointment only.
We are not open to the public on Tuesdays.
If you wish to make an appointment or if you have
questions about this change contact DiAnne
during regular business hours. Thank you <br />
    
      </p>
    </aside>

    <main class="main-content">
      <section class="text-box-container">
        <label class="text-box-label">Welcome</label>
        <p class="info-text">{{ preloadedText }}</p>
      </section>

      <section class="text-box-container">
        <label class="text-box-label">Featured Product</label>
        <p class="info-text">{{ featuredProductText }}</p>
      </section>
    </main>
  </div>
</template>

<style>
.home-body {
  display: flex;
  gap: 2rem;
  padding: var(--horizontal-page-padding);
  min-height: var(--home-height);
  box-sizing: border-box;
}

.sidebar {
  width: 250px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.text-box-container {
  max-width: 800px;
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