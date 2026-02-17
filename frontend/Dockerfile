FROM node:20-slim

WORKDIR /app

# Copy package files first
COPY package.json package-lock.json ./

# Clean install from your lockfile
RUN npm ci

COPY . .

# Run Next.js in development mode
CMD ["npm", "run", "dev"]