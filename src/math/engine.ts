export const MODULUS = 26
export const ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
export const AFFINE_UNITS = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25] as const
export type AffineKey = { a: number; b: number }
export type Permutation = [number, number, number, number]

export const S4: Permutation[] = [
  [0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1],
  [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3], [1, 0, 3, 2],
  [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0],
  [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0],
  [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1, 2], [3, 0, 2, 1],
  [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0],
]

export function mod(value: number, modulus = MODULUS): number {
  return ((value % modulus) + modulus) % modulus
}

export function gcd(left: number, right: number): number {
  let a = Math.abs(left)
  let b = Math.abs(right)
  while (b) [a, b] = [b, a % b]
  return a
}

export function modularInverse(value: number, modulus = MODULUS): number {
  for (let candidate = 1; candidate < modulus; candidate += 1) {
    if (mod(value * candidate, modulus) === 1) return candidate
  }
  throw new Error(`${value} has no inverse modulo ${modulus}.`)
}

export function caesarValue(value: number, shift: number): number {
  return mod(value + shift)
}

export function caesarText(text: string, shift: number): string {
  return [...text.toUpperCase()].map((character) => {
    const value = character.charCodeAt(0) - 65
    return value >= 0 && value < MODULUS ? ALPHABET[caesarValue(value, shift)] : character
  }).join('')
}

export function affineValue(value: number, key: AffineKey): number {
  if (!AFFINE_UNITS.includes(key.a as (typeof AFFINE_UNITS)[number])) {
    throw new Error(`a = ${key.a} is invalid: gcd(a, 26) must equal 1.`)
  }
  return mod(key.a * value + key.b)
}

export function affineText(text: string, key: AffineKey, decrypt = false): string {
  const operation = decrypt ? affineInverse(key) : key
  return [...text.toUpperCase()].map((character) => {
    const value = character.charCodeAt(0) - 65
    return value >= 0 && value < MODULUS ? ALPHABET[affineValue(value, operation)] : character
  }).join('')
}

export function affineCompose(first: AffineKey, second: AffineKey): AffineKey {
  return { a: mod(first.a * second.a), b: mod(first.a * second.b + first.b) }
}

export function affineInverse(key: AffineKey): AffineKey {
  const inverseA = modularInverse(key.a)
  return { a: inverseA, b: mod(-inverseA * key.b) }
}

export function permutationApply(permutation: Permutation, block: string): string {
  return permutation.map((index) => block[index] ?? '').join('')
}

export function permutationCompose(first: Permutation, second: Permutation): Permutation {
  return first.map((index) => second[index]) as Permutation
}

export function permutationInverse(permutation: Permutation): Permutation {
  const inverse = [0, 0, 0, 0] as Permutation
  permutation.forEach((value, index) => { inverse[value] = index })
  return inverse
}

export function permutationText(permutation: Permutation, text: string, decrypt = false): string {
  const operation = decrypt ? permutationInverse(permutation) : permutation
  const chars = [...text.toUpperCase()]
  const positions = chars.flatMap((character, index) => /^[A-Z]$/.test(character) ? [index] : [])
  const letters = positions.map((index) => chars[index])
  for (let start = 0; start + 3 < letters.length; start += 4) {
    const transformed = permutationApply(operation, letters.slice(start, start + 4).join(''))
    transformed.split('').forEach((character, offset) => { letters[start + offset] = character })
  }
  positions.forEach((position, index) => { chars[position] = letters[index] })
  return chars.join('')
}

export function permutationLabel(permutation: Permutation): string {
  return `[${permutation.map((value) => value + 1).join(', ')}]`
}

export function permutationIsValid(permutation: number[]): permutation is Permutation {
  return permutation.length === 4 && new Set(permutation).size === 4 && permutation.every((value) => value >= 0 && value < 4)
}

export function transformationOrder(apply: (value: number) => number, size: number): number {
  let current = Array.from({ length: size }, (_, index) => index)
  const identity = current.join(',')
  for (let order = 1; order <= 1000; order += 1) {
    current = current.map(apply)
    if (current.join(',') === identity) return order
  }
  return 0
}