<template>
  <div id="main-wrapper">
    <div class="header">

    </div>
    <div class="body">
      <card-table/>
    </div>
    <div class="footer">
      <hand-with-cards/>
    </div>
  </div>
</template>

<script>

import CardTable from "@/components/CardTable";
import HandWithCards from "@/components/HandWithCards";

export default {
  name: "MainWrapper",
  components: {CardTable, HandWithCards}

}
</script>

<style scoped>
  .header{
    height: 15%;
  }

  .body {
    height: 80%;
  }

  .footer{
    height: 5%;
  }


</style>