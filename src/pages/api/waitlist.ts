import type { APIRoute } from 'astro';
import { Resend } from 'resend';

export const prerender = false;

const NOTIFY_EMAIL = 'hello@aether8.ai';

const BUSINESS_LABELS: Record<string, string> = {
  real_estate: 'Real Estate',
  insurance: 'Insurance / Financial Services',
  home_services: 'Home Services',
  dental_medspa: 'Dental / Medspa',
  fitness: 'Fitness / Wellness',
  mortgage: 'Mortgage / Lending',
  other: 'Other',
};

export const POST: APIRoute = async ({ request }) => {
  // ── Parse body ──────────────────────────────────────────────────────────────
  let body: Record<string, string>;
  try {
    const ct = request.headers.get('content-type') ?? '';
    if (ct.includes('application/json')) {
      body = await request.json();
    } else {
      const fd = await request.formData();
      body = Object.fromEntries(fd.entries()) as Record<string, string>;
    }
  } catch {
    return Response.json({ error: 'Invalid request body.' }, { status: 400 });
  }

  const name = body.name?.trim();
  const email = body.email?.trim().toLowerCase();
  const businessType = body.business_type?.trim();
  const notes = body.notes?.trim() ?? '';

  // ── Validate ─────────────────────────────────────────────────────────────────
  if (!name || name.length < 2) {
    return Response.json({ error: 'Please enter your name.' }, { status: 422 });
  }
  if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return Response.json({ error: 'Please enter a valid email address.' }, { status: 422 });
  }
  if (!businessType || !BUSINESS_LABELS[businessType]) {
    return Response.json({ error: 'Please select your business type.' }, { status: 422 });
  }

  const businessLabel = BUSINESS_LABELS[businessType];

  // ── Resend ───────────────────────────────────────────────────────────────────
  const apiKey = import.meta.env.RESEND_API_KEY;
  if (!apiKey) {
    console.error('[waitlist] RESEND_API_KEY not set');
    return Response.json({ error: 'Server configuration error. Please email hello@aether8.ai directly.' }, { status: 500 });
  }

  const resend = new Resend(apiKey);

  try {
    // Internal notification
    await resend.emails.send({
      from: 'Scrnr Waitlist <hello@aether8.ai>',
      to: NOTIFY_EMAIL,
      subject: `New Scrnr Waitlist Signup — ${name}`,
      html: `
        <div style="font-family: system-ui, sans-serif; max-width: 560px; padding: 24px;">
          <h2 style="color: #111; margin-bottom: 16px;">New Scrnr Waitlist Signup</h2>
          <table style="width: 100%; border-collapse: collapse;">
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 10px 0; color: #666; width: 140px;">Name</td>
              <td style="padding: 10px 0; font-weight: 600; color: #111;">${name}</td>
            </tr>
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 10px 0; color: #666;">Email</td>
              <td style="padding: 10px 0; font-weight: 600; color: #111;">${email}</td>
            </tr>
            <tr style="border-bottom: 1px solid #eee;">
              <td style="padding: 10px 0; color: #666;">Business Type</td>
              <td style="padding: 10px 0; font-weight: 600; color: #111;">${businessLabel}</td>
            </tr>
            ${notes ? `
            <tr>
              <td style="padding: 10px 0; color: #666; vertical-align: top;">Notes</td>
              <td style="padding: 10px 0; color: #111;">${notes}</td>
            </tr>` : ''}
          </table>
          <p style="margin-top: 24px; color: #666; font-size: 14px;">
            Reply directly to this email to reach ${name} at ${email}.
          </p>
        </div>
      `,
      replyTo: email,
    });

    // Confirmation to submitter
    await resend.emails.send({
      from: 'Scrnr by Aether8 <hello@aether8.ai>',
      to: email,
      subject: "You're on the Scrnr waitlist",
      html: `
        <div style="font-family: system-ui, sans-serif; max-width: 560px; padding: 24px; color: #111;">
          <h2 style="margin-bottom: 8px;">You're on the list, ${name.split(' ')[0]}.</h2>
          <p style="color: #555; line-height: 1.6; margin-bottom: 20px;">
            Thanks for joining the Scrnr early access waitlist. We're working with a small group of
            ${businessLabel} businesses to configure and launch the first deployments.
          </p>
          <p style="color: #555; line-height: 1.6; margin-bottom: 20px;">
            We'll be in touch when a spot opens up. In the meantime, if you'd like to tell us more
            about your contact database or current workflow, just reply to this email.
          </p>
          <p style="color: #555; line-height: 1.6;">
            — The Aether8 team<br/>
            <a href="https://aether8.ai" style="color: #00d4ff;">aether8.ai</a>
          </p>
        </div>
      `,
    });

    return Response.json({ success: true }, { status: 200 });
  } catch (err) {
    console.error('[waitlist] Resend error:', err);
    return Response.json(
      { error: 'Failed to send confirmation. Please email hello@aether8.ai directly.' },
      { status: 500 }
    );
  }
};
