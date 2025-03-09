<script lang="ts">
    export let orders: { id: number; burgers: number; fries: number; drinks: number }[];
  </script>
  
  
  <h3>Order History</h3>
  
  {#if orders.length === 0}
    <p>No orders yet.</p>
  {:else}
    {#each orders as order}
      <div class="order-box">
        <strong>Order #{order.id}</strong>
        <span>{order.burgers} Burger(s), {order.fries} Fry(s), {order.drinks} Drink(s)</span>
      </div>
    {/each}
  {/if}
  
  <style>
    .order-box {
      display: flex;
      justify-content: space-between;
      padding: 10px;
      margin-top: 5px;
      border: 1px solid black;
      border-radius: 8px;
    }
  </style>
  