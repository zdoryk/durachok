<template>
  <img :src="icon"/>
</template>

<script>
import * as icons from "../assets/cards/SVG-cards-1.3";

export default {
  name: "IconComponent",
  props: ["name"],
  computed: {
    icon() {
      return icons[this.name]
    }
  },
}
</script>

<style scoped>

</style>