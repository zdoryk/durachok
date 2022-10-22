<template>
  <div class="card-table-card">
    <img :style="cssVars" class="card" :src="icon"/>
  </div>
</template>

<script>
import * as icons from "@/assets/cards/SVG-cards-1.3";
import {mapGetters} from "vuex";

export default {
  name: "CardTableCard",
  components: {},
  props: {
    card: Object,
  },
  data(){
    return{
    }
  },

  methods: {
    parseProxy(proxy){
      return JSON.parse(JSON.stringify(proxy))
    },
  },

  computed: {
    ...mapGetters({
      card_values: "CARD_VALUES"
    }),

    cardPath(){
      return "_" + this.card_values[this.card.card_rank] + "_of_" + this.card.card_suit
    },

    icon() {
      return icons[this.cardPath]
    },


    cssVars(){
      return{
        "--height": this.card.card_height + 'px',
      }
    }

  }
}
</script>

<style scoped lang="scss">
.text {
  color: white;
  font-size: 30px;
}


.card{
  height: var(--height);
  transition: 0.1s ease-in-out;
  bottom: 35px;
  //position: relative;
  //bottom: 520px;
}




</style>