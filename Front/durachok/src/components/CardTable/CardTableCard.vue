<template>
  <div class="card-table-card" :style="cssVars">
    <img :style="cssVars" class="card-trump" :src="icon" v-if="this.card.card_height===150"/>
    <img :style="cssVars" class="card" :src="icon" v-if="this.card.card_height===120"/>
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
    top_or_bot: {
      default: '',
      type: String
    }
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
      card_values: "CARD_VALUES",
      top_cards: "TOP_CARDS",
      bottom_cards: "BOTTOM_CARDS"
    }),

    cardPath(){
      return "_" + this.card_values[this.card.card_rank] + "_of_" + this.card.card_suit
    },

    icon() {
      return icons[this.cardPath]
    },

    positionMultiplier() {
      // console.log(this.top_or_bot)
      return 128
    },

    cardPosition(){
      return this.card.card_index * this.positionMultiplier
    },

    cssVars(){
      if (this.top_or_bot !== "top" && this.top_or_bot !== "bot"){
        return{
          "--height": this.card.card_height + 'px',
          "--position": "static",
        }
      } if ( this.top_or_bot === "top") {
        return {
          "--height": this.card.card_height + 'px',
          "--left": "-365px",
          // "--bottom": "20px",
          "--top": "100px",
          "--translate": "translate(" + this.cardPosition + "px, -10px)",
          "--position": "absolute"
        }
      } else {
        return {
          "--height": this.card.card_height + 'px',
          "--left": "10",
          // "--bottom": "35px",
          "--top": "85px",
          "--translate": "translate(" + this.cardPosition + "px, -10px)",
          "--position": "absolute"
        }
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

.card-trump, .card{
  height: var(--height);
  width: 80px;
  transition: 0.1s ease-in-out;
}


.card{
  position: var(--position);

  //position: var(--position);
  transform: var(--translate);
  //bottom: 520px;
  right: 300px;
  top: var(--top);
  left: var(--left);
  //bottom: var(--bottom);

}

.card-table-card{
  position: var(--position) ;

}




</style>
