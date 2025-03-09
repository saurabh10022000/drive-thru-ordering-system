<script lang="ts">
    export let totals: { burgers: number; fries: number; drinks: number };
  </script>
  
  
  <div class="total-box">
    <p>Total # of burgers</p>
    <p>{totals.burgers}</p>
  </div>
  <div class="total-box">
    <p>Total # of fries</p>
    <p>{totals.fries}</p>
  </div>
  <div class="total-box">
    <p>Total # of drinks</p>
    <p>{totals.drinks}</p>
  </div>
  
  <style>
    .total-box {
      padding: 20px;
      border: 1px solid black;
      border-radius: 12px;
      width: 150px;
      text-align: center;
    }
  </style>
  