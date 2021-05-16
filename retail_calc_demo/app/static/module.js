export default async () => {
  const statesUrl = new URL('/states', window.location.origin);
  const response = await fetch(statesUrl);
  const items = await response.json();
  if (items.length > 0) {
    const listHTML = items.map((item) => `<option>${item}</option>`).join('\n');
    const list = document.querySelector('.form-select');
    list.innerHTML = listHTML;
  }

  const calcUrl = new URL('/calc', window.location.origin);
  const form = document.querySelector('.row.g-3');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const url = new URL(calcUrl, window.location.origin);
    const elements = form.elements
    url.searchParams.append('quantity', elements['inputQuantity'].value);
    url.searchParams.append('price', elements['inputPrice'].value);
    url.searchParams.append('state_code', elements['inputState'].value);
    const response = await fetch(url);
    const items = await response.json();
    elements['outputSubtotal'].value = items['subtotal_with_discount'];
    elements['outputTotal'].value = items['total'];
  });
};