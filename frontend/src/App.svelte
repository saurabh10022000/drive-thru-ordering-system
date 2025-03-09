<script lang="ts">
  import Totals from "./components/Totals.svelte";
  import InputBox from "./components/InputBox.svelte";
  import OrderHistory from "./components/OrderHistory.svelte";
  import axios from "axios";

  let totals = { burgers: 0, fries: 0, drinks: 0 };
  let orders: { id: number; burgers: number; fries: number; drinks: number }[] = [];

  async function handleInput(e: CustomEvent<string>) {
    const message = e.detail; // ✅ Get the message from event.detail
    try {
      const response = await axios.post(
        "http://localhost:8000/process",
        { message },
        {
          headers: {
            "Content-Type": "application/json"
          }
        }
      );
      totals = response.data.totals;
      orders = response.data.orders;
    } catch (error) {
      console.error("Error:", error);
      alert("Failed to process the request.");
    }
  }
</script>


<style>
  main {
    max-width: 800px;
    margin: auto;
    padding: 20px;
    border: 2px solid black;
    border-radius: 12px;
  }
  .totals {
    display: flex;
    justify-content: space-around;
    margin-bottom: 20px;
  }
  .input-section {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
  }
</style>

<main>
  <div class="totals">
    <Totals {totals} />
  </div>

  <div class="input-section">
    <InputBox on:submit={handleInput} />
  </div>

  <OrderHistory {orders} />
</main>
