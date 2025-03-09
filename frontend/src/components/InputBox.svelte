<script lang="ts">
  import { createEventDispatcher } from 'svelte';
  const dispatch = createEventDispatcher();
  let message = '';

  function submit() {
    if (message.trim()) {
      dispatch('submit', message);
      message = '';
    }
  }
</script>

<textarea
  placeholder='Example: "I would like one burger and fries"'
  bind:value={message}
  rows="3"
></textarea>
<button on:click={submit}>Run</button>

<style>
  textarea {
    flex: 1;
    padding: 10px;
  }
  button {
    margin-left: 10px;
    padding: 10px 20px;
  }
</style>
