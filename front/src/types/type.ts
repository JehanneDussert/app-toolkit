// interface: object structure
// type: union or intersections

export interface User {
	id: number;
	name: string;
	email: string;
}

export type UserRole = 'admin' | 'user' | 'guest';
