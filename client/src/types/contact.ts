// client/src/types/contact.ts

export interface Contact {
  id: number;
  first_name: string;
  last_name: string;
  role: string | null;
  company: string | null;
  city: string;
  state_country: string;
  latitude: number | null;
  longitude: number | null;
  starred: boolean;
  created_at: string;
  updated_at: string;
  email: string | null;
  linkedin_url: string | null;
}

export interface Interaction {
  id: number;
  contact_id: number;
  interaction_date: string;
  notes: string | null;
  // `embedding` intentionally omitted: backend-only, used for vector search
}

export interface Connection {
  source_contact_id: number;
  target_contact_id: number;
  relationship_label: string | null;
}