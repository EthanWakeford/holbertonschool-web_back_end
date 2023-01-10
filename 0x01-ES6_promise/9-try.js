export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (ex) {
    queue.push('Error: '.concat(ex.message));
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
