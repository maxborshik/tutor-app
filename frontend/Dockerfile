FROM node:20-slim

WORKDIR /app/frontend

# Copy package files first
COPY package.json package-lock.json ./

# Clean install from your lockfile
RUN npm ci

# Run Next.js in development mode
CMD ["npm", "run", "dev"]